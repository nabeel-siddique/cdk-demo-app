from aws_cdk import core
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_ecs_patterns as ecs_patterns


class CdkDemoAppStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        vpc = ec2.Vpc(self, "MyVpc", max_azs=2)
        cluster = ecs.Cluster(self, "MyCluster", vpc=vpc)

        task_def = ecs.FargateTaskDefinition(
            self, "TaskDef")

        app_container = task_def.add_container("AppContainer",
                                               #   image=ecs.ContainerImage.from_asset(
                                               #       "myapp")
                                               image=ecs.ContainerImage.from_registry(
                                                   "mystique/predict-attire-for-weather")
                                               )

        app_container.add_port_mappings(
            ecs.PortMapping(container_port=80, protocol=ecs.Protocol.TCP)
        )

        myService = ecs_patterns.ApplicationLoadBalancedFargateService(self,
                                                                       "myService",
                                                                       cluster=cluster,
                                                                       desired_count=2,
                                                                       task_definition=task_def)
