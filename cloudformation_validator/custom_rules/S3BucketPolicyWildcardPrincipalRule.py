import inspect
import sys
from builtins import (str)
from cloudformation_validator.custom_rules.BaseRule import BaseRule

def lineno():
    """Returns the current line number in our program."""
    return str(' - S3BucketPolicyWildcardPrincipalRule - caller: '+str(inspect.stack()[1][3])+' - line number: '+str(inspect.currentframe().f_back.f_lineno))



class S3BucketPolicyWildcardPrincipalRule(BaseRule):


  def __init__(self, cfn_model=None, debug=None):
    '''
    Initialize
    :param cfn_model: 
    '''
    BaseRule.__init__(self, cfn_model, debug=debug)

  def rule_text(self):
    '''
    Get rule text
    :return: 
    '''
    if self.debug:
      print('rule_text'+lineno())
    return 'S3 Bucket policy should not allow * principal'


  def rule_type(self):
    '''
    Get rule type
    :return: 
    '''
    self.type= 'VIOLATION::FAILING_VIOLATION'
    return 'VIOLATION::FAILING_VIOLATION'

  def rule_id(self):
    '''
    Get rule id
    :return: 
    '''
    if self.debug:
      print('rule_id'+lineno())
    self.id ='F16'
    return 'F16'


  def audit_impl(self):
    '''
    Audit
    :return: violations 
    '''
    if self.debug:
      print('S3BucketPolicyWildcardPrincipalRule - audit_impl'+lineno())
    logical_resource_ids = []

    violating_policies = []
    resources = self.cfn_model.resources_by_type('AWS::S3::BucketPolicy')

    if len(resources) > 0:
      for resource in resources:
        if self.debug:
          print('resource: ' + str(resource) + lineno())

        if hasattr(resource, 'policy_document'):

          if resource.policy_document:
            if self.debug:
              print('has policy document ' + lineno())
              print(resource.policy_document.statements)

            if resource.policy_document.wildcard_allowed_principals():
              if self.debug:
                print('has wildcard allowsd principal'+lineno())

              violating_policies.append(str(resource.logical_resource_id))
    else:
      if self.debug:
        print('no violating_policies' + lineno())


    return violating_policies