Background:
Given smart contract "SC_AAA_BBB" deployado
    And contratante AAA Consultoria Empresarial Ltda. criada
    And contratada BBB Tecnologia Ltda. criada
    And data de criação é 01 de junho de 2026
    And data de inicio é 16 de junho de 2026
    And data de término é 16 de julho de 2026
    And contrato está criado
    And contrato está ativado
    And o valor do contrato é de 2000 reais

Scenario: Unsuccessful termination #1 of SC_AAA_BBB contract
Given o serviço não foi prestado pela contratada
When passou o dia 16 de julho de 2026
Then contrato deve ter status "UNSUCCESSFUL_TERMINATION"
    And Oblig1 deve ter status "DESCUMPRIDA"
    And Oblig2 deve ter status "TERMINADA"
    And Oblig3 deve ter status "TERMINADA"
    And Oblig4 deve ter status "TERMINADA"
    And Oblig5 deve ter status "TERMINADA"
    And Oblig6 deve ter status "TERMINADA"
    And Oblig7 deve ter status "TERMINADA"

Scenario: Unsuccessful termination #2 of SC_AAA_BBB contract
Given contratada não enviou o relatório de serviço
When passou o dia 16 de julho de 2026
Then contrato deve ter status "UNSUCCESSFUL_TERMINATION"
    And Oblig1 deve ter status "TERMINADA"
    And Oblig2 deve ter status "DESCUMPRIDA"
    And Oblig3 deve ter status "TERMINADA"
    And Oblig4 deve ter status "TERMINADA"
    And Oblig5 deve ter status "TERMINADA"
    And Oblig6 deve ter status "TERMINADA"
    And Oblig7 deve ter status "TERMINADA"

Scenario: Unsuccessful termination #3 of SC_AAA_BBB contract
Given contratante não pagou 1000,00 para a contratada
When passou dia 01 de junho de 2026
Then contrato deve ter status "UNSUCCESSFUL_TERMINATION"
    And Oblig1 deve ter status "TERMINADA"
    And Oblig2 deve ter status "TERMINADA"
    And Oblig3 deve ter status "TERMINADA"
    And Oblig4 deve ter status "DESCUMPRIDA"
    And Oblig5 deve ter status "TERMINADA"
    And Oblig6 deve ter status "ATIVA"
    And Oblig7 deve ter status "TERMINADA"

Scenario: Unsuccessful termination #4 of SC_AAA_BBB contract
Given contratante pagou apenas 1000,00 para a contratada
When passou dia 16 de julho de 2026
Then contrato deve ter status "UNSUCCESSFUL_TERMINATION"
    And Oblig1 deve ter status "TERMINADA"
    And Oblig2 deve ter status "TERMINADA"
    And Oblig3 deve ter status "TERMINADA"
    And Oblig4 deve ter status "TERMINADAf"
    And Oblig5 deve ter status "DESCUMPRIDA"
    And Oblig6 deve ter status "ATIVA"
    And Oblig7 deve ter status "TERMINADA"