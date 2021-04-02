#!/usr/bin/python3

'''
Copyright 2020 Josep Argelich
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
import random
from random import randint
from api_pb2 import Cnf

# Classes

class Clause():
    """A Boolean clause randomly generated"""

    def __init__(self, num_vars, clause_length):
        """
        Initialization
        length: Clause length
        lits: List of literals
        """
        self.length = clause_length
        self.lits = None
        self.gen_random_clause(num_vars)

    def gen_random_clause(self, num_vars):
        """ Generate random clause"""
        self.lits = []
        while len(self.lits) < self.length: # Set the variables of the clause
            new_lit = random.randint(1, num_vars) # New random variable
            if new_lit not in self.lits: #If the variable is not already in the clause
                self.lits.append(new_lit) # Add it to the clause
        for i in range(len(self.lits)): # Sets a negative sense with a 50% probability
            if random.random() < 0.5:
                self.lits[i] *= -1 # Change the sense of the literal
    

class CNF():
    """A CNF formula randomly generated"""

    def __init__(self, num_vars, num_clauses, clause_length):
        """
        Initialization
        num_vars: Number of variables
        num_clauses: Number of clauses
        clause_length: Length of the clauses
        clauses: List of clauses
        """
        self.num_vars = num_vars
        self.num_clauses = num_clauses
        self.clause_length = clause_length
        self.clauses = None
        self.gen_random_clauses()

    def gen_random_clauses(self):
        """Generate random clauses"""
        self.clauses = []
        for i in range(self.num_clauses):
            c = Clause(self.num_vars, self.clause_length)
            self.clauses.append(c)

    def ok(self):
        cnf = Cnf()
        for c in self.clauses:
            clause = cnf.clause.add()
            clause.literal.extend(c.lits)
        return cnf

def ok():
    cnf = CNF(randint(1,100),randint(1,100),3)
    return cnf.ok()
