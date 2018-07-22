import inspect
import sys
from builtins import (str)
from cloudformation_validator.custom_rules.BaseRule import BaseRule

def lineno():
    """Returns the current line number in our program."""
    return str(' - WafWebAclDefaultActionRule - caller: '+str(inspect.stack()[1][3])+' - line number: '+str(inspect.currentframe().f_back.f_lineno))


class WafWebAclDefaultActionRule(BaseRule):

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
    return 'WebAcl DefaultAction should not be ALLOW'


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
    self.id ='F665'
    return 'F665'


  def audit_impl(self):
    '''
    Audit
    :return: violations 
    '''
    if self.debug:
      print('WafWebAclDefaultActionRule - audit_impl'+lineno())
    
    violating_web_acls = []
    resources = self.cfn_model.resources_by_type('AWS::WAF::WebACL')

    if len(resources)>0:
      for resource in resources:
          if self.debug:
            print('resource: '+str(resource)+lineno())

          if hasattr(resource,'defaultAction'):
            if resource.defaultAction:
              if self.debug:
                print('defaultAction: '+str(resource.defaultAction))
              if resource.defaultAction['Type'] == 'ALLOW':

                violating_web_acls.append(str(resource.logical_resource_id))

    else:
      if self.debug:
        print('no violating_web_acls' + lineno())

    return violating_web_acls