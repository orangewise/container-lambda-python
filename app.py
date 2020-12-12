#!/usr/bin/env python3

from aws_cdk import core

from container_lambda_python.container_lambda_python_stack import ContainerLambdaPythonStack


app = core.App()
ContainerLambdaPythonStack(app, "container-lambda-python")

app.synth()
