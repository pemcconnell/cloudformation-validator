import os
import unittest
import sys
from collections import OrderedDict
from cloudformation_validator.ValidateUtility import ValidateUtility as class_to_test


def pretty(value, htchar='\t', lfchar='\n', indent=0):
    nlch = lfchar + htchar * (indent + 1)
    if type(value) == type(dict()) or type(value)== type(OrderedDict()):

        items = [
            nlch + repr(key) + ': ' + pretty(value[key], htchar, lfchar, indent + 1)
            for key in value
        ]
        return '{%s}' % (','.join(items) + lfchar + htchar * indent)
    elif type(value) == type(list()):
        items = [
            nlch + pretty(item, htchar, lfchar, indent + 1)
            for item in value
        ]
        return '[%s]' % (','.join(items) + lfchar + htchar * indent)
    elif type(value) is tuple:
        items = [
            nlch + pretty(item, htchar, lfchar, indent + 1)
            for item in value
        ]
        return '(%s)' % (','.join(items) + lfchar + htchar * indent)
    else:

        print('repr'+str(repr(value)))
        return repr(value)

class TestEc2Instance(unittest.TestCase):
    """
    Test ec2 instance
    """

    def test_ec2_instance_no_tags(self):

      expected_result =  {
            'failure_count': '1',
            'filename': '/json/ec2_instance/no_tags.json',
            'file_results': [
                {
                    'id': 'F86',
                    'type': 'VIOLATION::FAILING_VIOLATION',
                    'message': 'EC2 instance does not have the required tags of Name, ResourceOwner, DeployedBy, Project',
                    'logical_resource_ids': [
                        'EC2I4LBA1'
                    ]
                }
            ]
        }

      if sys.version_info[0] < 3:

          new_file_results = []

          if 'file_results' in expected_result:
              for info in expected_result['file_results']:
                  print('info: ' + str(info))
                  print('type: ' + str(type(info)))
                  order_of_keys = ["id", "type", "message", "logical_resource_ids"]
                  list_of_tuples = [(key, info[key]) for key in order_of_keys]
                  new_results = OrderedDict(list_of_tuples)
                  new_file_results.append(new_results)
              print('new file results: ' + str(new_file_results))
              expected_result['file_results'] = new_file_results

          order_of_keys = ["failure_count", "filename", "file_results"]
          list_of_tuples = [(key, expected_result[key]) for key in order_of_keys]
          expected_result = OrderedDict(list_of_tuples)



      expected_result = pretty(expected_result)

      template_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'/cloudformation_validator/test_templates/json/ec2_instance/no_tags.json'
      debug = False

      config_dict = {}
      config_dict['template_file'] = template_name
      config_dict['debug'] = debug
      config_dict['profile'] = None
      config_dict['rules_directory'] = None
      config_dict['input_path'] = None
      config_dict['profile'] = None
      config_dict['allow_suppression'] = False
      config_dict['print_suppression'] = False
      config_dict['parameter_values_path'] = None
      config_dict['isolate_custom_rule_exceptions'] = None
      config_dict['use_optional_rules'] = True
      validator = class_to_test(config_dict)

      real_result =  validator.validate()
      self.maxDiff = None

      print('expected results: '+str(expected_result))
      print('real results: '+str(real_result))

      self.assertEqual(expected_result, real_result)



    def test_ec2_instance_has_required_tags(self):

      expected_result =  {
        'failure_count': '0',
        'filename': '/json/ec2_instance/has_required_tags.json',
        'file_results': [

            ]
        }


      if sys.version_info[0] < 3:

          new_file_results = []

          if 'file_results' in expected_result:
              for info in expected_result['file_results']:
                  print('info: ' + str(info))
                  print('type: ' + str(type(info)))
                  order_of_keys = ["id", "type", "message", "logical_resource_ids"]
                  list_of_tuples = [(key, info[key]) for key in order_of_keys]
                  new_results = OrderedDict(list_of_tuples)
                  new_file_results.append(new_results)
              print('new file results: ' + str(new_file_results))
              expected_result['file_results'] = new_file_results

          order_of_keys = ["failure_count", "filename", "file_results"]
          list_of_tuples = [(key, expected_result[key]) for key in order_of_keys]
          expected_result = OrderedDict(list_of_tuples)


      expected_result = pretty(expected_result)



      template_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'/cloudformation_validator/test_templates/json/ec2_instance/has_required_tags.json'
      debug = False

      config_dict = {}
      config_dict['template_file'] = template_name
      config_dict['debug'] = debug
      config_dict['profile'] = None
      config_dict['rules_directory'] = None
      config_dict['input_path'] = None
      config_dict['profile'] = None
      config_dict['allow_suppression'] = False
      config_dict['print_suppression'] = False
      config_dict['parameter_values_path'] = None
      config_dict['isolate_custom_rule_exceptions'] = None
      config_dict['use_optional_rules'] = True
      validator = class_to_test(config_dict)

      real_result =  validator.validate()
      self.maxDiff = None

      print('expected results: '+str(expected_result))
      print('real results: '+str(real_result))

      self.assertEqual(expected_result, real_result)


    def test_ec2_instance_missing_one_tags(self):

      expected_result =  {
            'failure_count': '1',
            'filename': '/json/ec2_instance/missing_one_required_tags.json',
            'file_results': [
                {
                    'id': 'F86',
                    'type': 'VIOLATION::FAILING_VIOLATION',
                    'message': 'EC2 instance does not have the required tags of Name, ResourceOwner, DeployedBy, Project',
                    'logical_resource_ids': [
                        'EC2I4LBA2'
                    ]
                }
            ]
        }

      if sys.version_info[0] < 3:

          new_file_results = []

          if 'file_results' in expected_result:
              for info in expected_result['file_results']:
                  print('info: ' + str(info))
                  print('type: ' + str(type(info)))
                  order_of_keys = ["id", "type", "message", "logical_resource_ids"]
                  list_of_tuples = [(key, info[key]) for key in order_of_keys]
                  new_results = OrderedDict(list_of_tuples)
                  new_file_results.append(new_results)
              print('new file results: ' + str(new_file_results))
              expected_result['file_results'] = new_file_results

          order_of_keys = ["failure_count", "filename", "file_results"]
          list_of_tuples = [(key, expected_result[key]) for key in order_of_keys]
          expected_result = OrderedDict(list_of_tuples)



      expected_result = pretty(expected_result)

      template_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'/cloudformation_validator/test_templates/json/ec2_instance/missing_one_required_tags.json'
      debug = False

      config_dict = {}
      config_dict['template_file'] = template_name
      config_dict['debug'] = debug
      config_dict['profile'] = None
      config_dict['rules_directory'] = None
      config_dict['input_path'] = None
      config_dict['profile'] = None
      config_dict['allow_suppression'] = False
      config_dict['print_suppression'] = False
      config_dict['parameter_values_path'] = None
      config_dict['isolate_custom_rule_exceptions'] = None
      config_dict['use_optional_rules'] = True
      validator = class_to_test(config_dict)

      real_result =  validator.validate()
      self.maxDiff = None

      print('expected results: '+str(expected_result))
      print('real results: '+str(real_result))

      self.assertEqual(expected_result, real_result)

