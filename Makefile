.EXPORT_ALL_VARIABLES:

PYTHONUNBUFFERED=1
POETRY_VERSION=2.2.1
POETRY ?= poetry@$(POETRY_VERSION)

.PHONY: install-poetry
install-poetry:
	@pipx install --suffix="@$(POETRY_VERSION)" "poetry==$(POETRY_VERSION)"
	$(POETRY) --version

.PHONY: install
install:
	$(POETRY) sync --all-extras $(opts)

.PHONY: update
update: update-lock install

.PHONY: update-lock
update-lock:
	$(POETRY) update --lock -v

.PHONY: lint-black
lint-black:
	$(POETRY) run black --check --diff .

.PHONY: lint-flake8
lint-flake8:
	$(POETRY) run flake8

.PHONY: lint-isort
lint-isort:
	$(POETRY) run isort --check-only --diff .

.PHONY: lint-mypy
lint-mypy:
	$(POETRY) run mypy

.PHONY: lint-python
lint-python: lint-black lint-isort lint-mypy

.PHONY: lint
lint: lint-python

.PHONY: fmt-black
fmt-black:
	$(POETRY) run black .

.PHONY: fmt-isort
fmt-isort:
	$(POETRY) run isort .

.PHONY: fmt
fmt: fmt-black fmt-isort

.PHONY: build
build:
	$(POETRY) build
# 	$(POETRY) build -f sdist    # build source distribution only

.PHONY: publish
publish:
	$(POETRY) publish

.PHONY: grpc-stubs
grpc-stubs:
	python -m grpc_tools.protoc \
	  --proto_path=./protos \
	  --python_out=. \
	  --grpc_python_out=. \
	  --mypy_out=. \
	  protos/axonclient/protos/common.proto \
	  protos/axonclient/protos/command.proto \
	  protos/axonclient/protos/control.proto \
	  protos/axonclient/protos/event.proto \
	  protos/axonclient/protos/query.proto \
	  protos/axonclient/protos/dcb.proto

.PHONY: start-axon-server-aggregates
start-axon-server-aggregates:
	docker run -d --name my-axon-server -p 8024:8024 -p 8124:8124 axoniq/axonserver axonserver
	@printf "Waiting for Axon Server to initialize"
	@until curl -sf -X POST "http://127.0.0.1:8024/v2/cluster/init" \
	      | grep -q "Accepted init cluster request"; do \
		printf "."; \
		sleep 1; \
	done
	@echo " done."


.PHONY: stop-axon-server-aggregates
stop-axon-server-aggregates:
	docker stop my-axon-server
	docker rm my-axon-server

.PHONY: start-axon-server-dcb
start-axon-server-dcb:
	docker run -d \
	  --name my-axon-dcb-server \
	  -p 8024:8024 \
	  -p 8124:8124 \
	  -e AXONIQ_AXONSERVER_NAME=my-axon-dcb-server \
	  -e AXONIQ_AXONSERVER_HOSTNAME=my-axon-dcb-server \
	  -e AXONIQ_AXONSERVER_DCB_ENABLED="true" \
	  -e AXONIQ_AXONSERVER_CLUSTER_MODE="SINGLE_NODE" \
	  axoniq/axonserver
#	  axoniq/axonserver:latest-jdk-17-nonroot
	@printf "Waiting for Axon Server to initialize DCB"
	@until curl -sf -X POST "http://127.0.0.1:8024/v2/cluster/init?dcb=true" \
	      | grep -q "Accepted init cluster request"; do \
		printf "."; \
		sleep 1; \
	done
	@echo " done."

.PHONY: stop-axon-server-dcb
stop-axon-server-dcb:
	docker stop my-axon-dcb-server
	docker rm my-axon-dcb-server

.PHONY: test-axon-client-aggregates
test-axon-client-aggregates:
	$(POETRY) run python -m unittest -v tests.test_axonclient.TestAxonClientWithAggregatesAPI

.PHONY: test-axon-client-dcb
test-axon-client-dcb:
	$(POETRY) run python -m unittest -v tests.test_axonclient.TestAxonClientWithDCBAPI

.PHONY: test
test: start-axon-server-aggregates test-axon-client-aggregates stop-axon-server-aggregates start-axon-server-dcb test-axon-client-dcb stop-axon-server-dcb

