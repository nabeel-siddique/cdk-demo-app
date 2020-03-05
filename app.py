#!/usr/bin/env python3

from aws_cdk import core

from cdk_demo_app.cdk_demo_app_stack import CdkDemoAppStack


app = core.App()
CdkDemoAppStack(app, "cdk-demo-app")

app.synth()
