Background:
Given smart contract "SC_AAA_BBB" deployado
    And contratante AAA Consultoria Empresarial Ltda. criada
    And contratada BBB Tecnologia Ltda. criada

Scenario: Create the SC_AAA_BBB contract
Given data de criação é 01 de junho de 2026
    And data de inicio é 16 de junho de 2026
    And data de término é 16 de julho de 2026
    And Oblig 1 é "Prestar os serviços contratados"
    And Oblig 2 é "Enviar fatura e relatório das horas prestadas"
    And Oblig 3 é "Indicar um colaborador responsável pelos contatos de ordem técnica com a Contratada"
    And Oblig 4 é "Realizar o pagamento de 50% do serviço desenvolvido na assinatura do contrato"
    And Oblig 5 é "Realizar o pagamento de 50% do serviço desenvolvido trinta dias após o início dos trabalhos"
    And Oblig 6 é "As parcelas não liquidadas nos respectivos vencimentos ficarão sujeitas à multa"
    And Oblig 7 é "Dispor para a contratada, após o período de garantia (90 dias após a entrega), um pacote de 20 horas mensais ao valor de 120 reais a hora"
When contrato "SC_AAA_BBB" é criado
Then contrato "SC_AAA_BBB" deve ter status "CRIADO"
    And a Oblig1 deve ter status "CRIADO"
    And a Oblig2 deve ter status "CRIADO"
    And a Oblig3 deve ter status "CRIADO"
    And a Oblig4 deve ter status "CRIADO"
    And a Oblig5 deve ter status "CRIADO"
    And a Oblig6 deve ter status "CRIADO"
    And a Oblig7 deve ter status "CRIADO"
    And o contrato não deve estar no status "ATIVO"

Scenario: Activate the SC_AAA_BBB contract
Given data de criação é 01 de junho de 2026
    And o contrato "SC_AAA_BBB" é criado
When o contrato é ativado
    And a data de ativação é 16 de junho de 2026
Then contrato deve ter status "ATIVO"
    And Oblig1 deve ter status "ATIVO"
    And Oblig2 deve ter status "ATIVO"
    And Oblig3 deve ter status "ATIVO"
    And Oblig4 deve ter status "ATIVO"
    And Oblig5 deve ter status "ATIVO"
    And Oblig6 deve ter status "ATIVO"
    And Oblig7 deve ter status "CRIADO"