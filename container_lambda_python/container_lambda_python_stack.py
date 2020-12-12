from aws_cdk import core
import aws_cdk.aws_lambda as lambda_
import os.path

dirname = os.path.dirname(__file__)


class ContainerLambdaPythonStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fnc = lambda_.DockerImageFunction(
            self,
            "AssetFunction",
            code=lambda_.DockerImageCode.from_image_asset(
                os.path.join(dirname, "docker-handler")
            ),
        )