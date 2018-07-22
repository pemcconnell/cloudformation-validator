import inspect
import sys
from cloudformation_validator.RuleDefinition import RuleDefinition
from collections import OrderedDict



def lineno():
    """Returns the current line number in our program."""
    return str(' - Violation - line number: '+str(inspect.currentframe().f_back.f_lineno))



class Violation(RuleDefinition):

    def __init__(self, id, type, message, logical_resource_ids=None, debug=False):
        '''
        Initialize Violation
        :param id: 
        :param type: 
        :param message: 
        :param logical_resource_ids: 
        :param debug: 
        '''
        RuleDefinition.__init__(self, id, type, message)
        self.attr_reader = None
        self.message = message
        self.type = type
        self.logical_resource_ids= logical_resource_ids
        self.id=id
        self.debug = debug

        if self.debug:
            print('Violation - init'+lineno())


    def to_string(self):
        '''
        Returns violation as a string
        :return: 
        '''
        if self.debug:
            print('to string'+lineno())
        #FIXME
        sys.exit(1)
        #"#{super} #{@logical_resource_ids}"


    def to_hash(self):
        '''
        Converts violation to hash
        :return: 
        '''
        if self.debug:
            print('to hash'+lineno())
            print('logical id type: '+str(type(self.logical_resource_ids))+lineno())
            print('message: '+str(self.message))



        hash = {'id': self.id,'type':self.type ,'message': self.message, 'logical_resource_ids': self.logical_resource_ids}

        order_of_keys = ["id", "type", "message","logical_resource_ids"]
        list_of_tuples = [(key, hash[key]) for key in order_of_keys]
        new_results = OrderedDict(list_of_tuples)



        if self.debug:
            print('hash is: '+str(new_results)+lineno())

        return new_results