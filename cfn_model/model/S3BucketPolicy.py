from cfn_model.model.ModelElement import ModelElement



class S3BucketPolicy(ModelElement):

    def __init__(self, cfn_model):
        '''
        Initialize
        :param cfn_model: 
        '''
        ModelElement.__init__(self, cfn_model)
        self.policy_document = None
        self.resource_type = 'AWS::S3::BucketPolicy'



