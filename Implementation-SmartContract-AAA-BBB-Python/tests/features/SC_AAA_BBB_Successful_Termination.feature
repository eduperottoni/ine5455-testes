Feature: SC_AAA_BBB Successful Termination


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

Scenario: Successful termination #1 of SC_AAA_BBB contract
Given contratada entregou o serviço em 16 de julho de 2026
    And contratante pagou 1000 reais em 01 de junho de 2026
    And contratante pagou 1000 reais em 01 de julho de 2026
Then contrato deve ter status "SUCCESSFUL_TERMINATION"
    And Oblig1 deve ter status "OBEDECIDO"
    And Oblig4 deve ter status "OBEDECIDO"
    And Oblig5 deve ter status "OBEDECIDO"
    And Oblig7 deve ter status "ATIVO"