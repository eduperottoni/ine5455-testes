Feature: SC_AAA_BBB Successful Termination

Background:
Given contratante AAA criada
    And contratada BBB criada
    And data de criação é 1
    And contrato foi criado
    And o contrato é ativado

Scenario: Successful termination #1 of SC_AAA_BBB contract
Given Oblig1 foi cumprida
    And Oblig4 foi cumprida
    And Oblig5 foi cumprida
When o contrato é encerrado
Then contrato deve ter status 2
    And Oblig1 deve ter status 2
    And Oblig4 deve ter status 2
    And Oblig5 deve ter status 2
    And Oblig7 deve ter status 1
