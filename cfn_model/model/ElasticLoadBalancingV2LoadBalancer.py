from cfn_model.model.ModelElement import ModelElement

class ElasticLoadBalancingV2LoadBalancer(ModelElement):

    def __init__(self, cfn_model):
        '''
        Initialize
        :param cfn_model: 
        '''
        ModelElement.__init__(self, cfn_model)

        self.securityGroups = []
        self.security_groups = []
        self.loadBalancerAttributes = []
        self.subnets = []
        self.tags = []
        self.resource_type = 'AWS::ElasticLoadBalancingV2::LoadBalancer'