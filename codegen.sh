#!/bin/bash

pushd src/
# generate code from the proto files
python3 - m grpc_tools.protoc - Iproto / --python_out = . --grpc_python_out = . proto/accounts/v1/gvoice.proto
popd
