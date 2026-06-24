Feature: SC_AAA_BBB Unsuccessful Termination

Background:
Given contratante AAA criada
    And contratada BBB criada
    And data de criação é 1
    And contrato foi criado
    And o contrato é ativado

Scenario: Unsuccessful termination #1 of SC_AAA_BBB contract
Given Oblig1 não foi cumprida
    And Oblig2 foi cumprida
    And Oblig4 foi cumprida
    And Oblig5 foi cumprida
When o contrato é encerrado
Then contrato deve ter status 3
    And Oblig1 deve ter status 4
    And Oblig2 deve ter status 4
    And Oblig3 deve ter status 4
    And Oblig4 deve ter status 4
    And Oblig5 deve ter status 4
    And Oblig6 deve ter status 4
    And Oblig7 deve ter status 4

Scenario: Unsuccessful termination #2 of SC_AAA_BBB contract
Given Oblig1 foi cumprida
    And Oblig2 não foi cumprida
    And Oblig4 foi cumprida
    And Oblig5 foi cumprida
When o contrato é encerrado
Then contrato deve ter status 3
    And Oblig1 deve ter status 4
    And Oblig2 deve ter status 4
    And Oblig3 deve ter status 4
    And Oblig4 deve ter status 4
    And Oblig5 deve ter status 4
    And Oblig6 deve ter status 4
    And Oblig7 deve ter status 4

Scenario: Unsuccessful termination #3 of SC_AAA_BBB contract
Given Oblig1 foi cumprida
    And Oblig2 foi cumprida
    And Oblig4 não foi cumprida
    And Oblig5 foi cumprida
When o contrato é encerrado
Then contrato deve ter status 3
    And Oblig1 deve ter status 4
    And Oblig2 deve ter status 4
    And Oblig3 deve ter status 4
    And Oblig4 deve ter status 4
    And Oblig5 deve ter status 4
    And Oblig6 deve ter status 4
    And Oblig7 deve ter status 4

Scenario: Unsuccessful termination #4 of SC_AAA_BBB contract
Given Oblig1 foi cumprida
    And Oblig2 foi cumprida
    And Oblig4 foi cumprida
    And Oblig5 não foi cumprida
When o contrato é encerrado
Then contrato deve ter status 3
    And Oblig1 deve ter status 4
    And Oblig2 deve ter status 4
    And Oblig3 deve ter status 4
    And Oblig4 deve ter status 4
    And Oblig5 deve ter status 4
    And Oblig6 deve ter status 4
    And Oblig7 deve ter status 4
