#!/usr/bin/env python3
import os

import aws_cdk as cdk

from kb.stack import KnowledgeBase
from twin.stack import Twin

env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region='us-west-2')
app = cdk.App()
kb = KnowledgeBase(app, "KnowledgeBaseStack", env=env)
_ = Twin(app, "Twin",
         kb_arn=kb.kb.knowledge_base_arn,
         kb_id=kb.kb.knowledge_base_id,
         kb_data_src_id=kb.kb.data_source_id,
         kb_input_bucket=kb.input_bucket,
         env=env,
         custom_domain_name="twin.saraselvaraju.com",
         custom_certificate_arn="arn:aws:acm:us-east-1:756821799753:certificate/cdadcf69-40a2-4634-a68b-96a52627de7a",
        )

app.synth()
