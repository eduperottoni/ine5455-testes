Feature: SC_AAA_BBB Creation

Background:
Given contratante AAA criada
    And contratada BBB criada

Scenario: Create the SC_AAA_BBB contract
Given data de criação é 1
When contrato é criado
Then contrato deve ter status 0
    And data de criação é 1
    And data de inicio é 16
    And data de término é 46
    And Oblig1 deve ter status 0
    And Oblig2 deve ter status 0
    And Oblig3 deve ter status 0
    And Oblig4 deve ter status 0
    And Oblig5 deve ter status 0
    And Oblig6 deve ter status 0
    And Oblig7 deve ter status 0

Scenario: Activate the SC_AAA_BBB contract
Given data de criação é 1
    And contrato foi criado
When o contrato é ativado
    And a data de ativação é 16
Then contrato deve ter status "ATIVO"
    And Oblig1 deve ter status "ATIVO"
    And Oblig2 deve ter status "ATIVO"
    And Oblig3 deve ter status "ATIVO"
    And Oblig4 deve ter status "ATIVO"
    And Oblig5 deve ter status "ATIVO"
    And Oblig6 deve ter status "ATIVO"
    And Oblig7 deve ter status "CRIADO"