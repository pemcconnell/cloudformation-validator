from cfn_model.model.ModelElement import ModelElement


class EC2SecurityGroupIngress(ModelElement):

    def __init__(self, cfn_model,debug=False):
        '''
        Initialize
        :param cfn_model: 
        :param debug: 
        '''
        self.debug = debug

        if self.debug:
            print('EC2SecurityGroupIngress __init__')
        ModelElement.__init__(self, cfn_model)

        self.resource_type = 'AWS::EC2::SecurityGroupIngress'