Feature: SC_AAA_BBB Creation

Background:
Given the client named AAA
And the contractor named BBB
And the creation date is 10


#Scenario: Create the SC_AAA_BBB contract
#COMPLETAR


Scenario: Activate the SC_AAA_BBB contract
Given I have created and deployed the smart contract 
When I activate the smart contract
Then the smart contract is activated
And creation date is 10
#COMPLETAR


