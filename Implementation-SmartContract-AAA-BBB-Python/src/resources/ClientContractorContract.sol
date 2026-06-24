pragma solidity 0.8.0;

contract ClientContractorContract {
    
    address owner = msg.sender; //dono do contrato é o criador

    enum Status { Created, InEffect, SuccessfulTermination, UnsuccessfulTermination }
    enum ObligStatus { Created, Active, Fullfilled, Unfulfilled, Inactive }
    
    Status status;

    struct Oblig {
        string description;
        ObligStatus status;
    }
    
    string client;
    string contractor;
    int creationDate;
    int activationDate;
    int terminationDate;
    Oblig oblig1;
    Oblig oblig2;
    Oblig oblig3;
    Oblig oblig4;
    Oblig oblig5;
    Oblig oblig6;
    Oblig oblig7;

    // INCOMPLETO

    constructor( string memory _client, string memory _contractor, int _creationDate ) public {
        client = _client;
        contractor = _contractor;
    	creationDate = _creationDate;
        activationDate = creationDate + 15;
        terminationDate = activationDate + 30;
        status = Status.Created;
        oblig1 = Oblig(unicode"Prestar os serviços contratados", ObligStatus.Created);
        oblig2 = Oblig(unicode"Enviar fatura e relatório das horas prestadas", ObligStatus.Created);
        oblig3 = Oblig(unicode"Indicar um colaborador responsável pelos contatos de ordem técnica com a Contratada", ObligStatus.Created);
        oblig4 = Oblig(unicode"Realizar o pagamento de 50% do serviço desenvolvido na assinatura do contrato", ObligStatus.Created);
        oblig5 = Oblig(unicode"Realizar o pagamento de 50% do serviço desenvolvido trinta dias após o início dos trabalhos", ObligStatus.Created);
        oblig6 = Oblig(unicode"As parcelas não liquidadas nos respectivos vencimentos ficarão sujeitas à multa", ObligStatus.Created);
        oblig7 = Oblig(unicode"Dispor para a contratada, após o período de garantia (90 dias após a entrega), um pacote de 20 horas mensais ao valor de 120 reais a hora", ObligStatus.Created);
    }

    //SETTERS

    // Transição Activate (diagrama de estados AAA-BBB): ao ativar o contrato,
    // as obrigações oblig1..oblig6 são ativadas. A oblig7 é uma obrigação
    // "sobrevivente": só é ativada na entrada do estado Successful Termination.
   	function activate () public {
        require(status == Status.Created, unicode"O contrato precisa estar em 'Created' para ser ativado");
    	status = Status.InEffect;
        oblig1.status = ObligStatus.Active;
        oblig2.status = ObligStatus.Active;
        oblig3.status = ObligStatus.Active;
        oblig4.status = ObligStatus.Active;
        oblig5.status = ObligStatus.Active;
        oblig6.status = ObligStatus.Active;
    }

    // Marca uma obrigação (1..7) como cumprida.
    function fulfillOblig(uint8 number) public {
        setObligStatus(number, ObligStatus.Fullfilled);
    }

    // Marca uma obrigação (1..7) como descumprida.
    function unfulfillOblig(uint8 number) public {
        setObligStatus(number, ObligStatus.Unfulfilled);
    }

    function setObligStatus(uint8 number, ObligStatus newStatus) internal {
        if (number == 1) { oblig1.status = newStatus; }
        else if (number == 2) { oblig2.status = newStatus; }
        else if (number == 3) { oblig3.status = newStatus; }
        else if (number == 4) { oblig4.status = newStatus; }
        else if (number == 5) { oblig5.status = newStatus; }
        else if (number == 6) { oblig6.status = newStatus; }
        else if (number == 7) { oblig7.status = newStatus; }
        else { revert(unicode"Obrigação inexistente (use 1..7)"); }
    }

    // Verifica se uma obrigação específica está cumprida.
    function isObligFulfilled(uint8 number) public view returns (bool) {
        return getObligStatus(number) == ObligStatus.Fullfilled;
    }

    // Transição FulfillActiveObligations: encerra o contrato com SUCESSO quando as
    // obrigações essenciais (oblig1 E oblig4 E oblig5) estão cumpridas. Na entrada do
    // estado Successful Termination a obrigação sobrevivente (oblig7) é ativada.
    //
    // Transição Terminate: encerra SEM sucesso quando alguma obrigação essencial não
    // foi cumprida (~oblig1 OU ~oblig2 OU ~oblig4 OU ~oblig5). Nesse caso todas as
    // obrigações são encerradas (Inactive).
    function terminate () public {
        require(status == Status.InEffect, unicode"O contrato precisa estar em vigor para ser encerrado");
        if (isObligFulfilled(1) && isObligFulfilled(2) && isObligFulfilled(4) && isObligFulfilled(5)) {
            status = Status.SuccessfulTermination;
            oblig7.status = ObligStatus.Active; // obrigação sobrevivente ativada na entrada
        } else {
            status = Status.UnsuccessfulTermination;
            oblig1.status = ObligStatus.Inactive;
            oblig2.status = ObligStatus.Inactive;
            oblig3.status = ObligStatus.Inactive;
            oblig4.status = ObligStatus.Inactive;
            oblig5.status = ObligStatus.Inactive;
            oblig6.status = ObligStatus.Inactive;
            oblig7.status = ObligStatus.Inactive;
        }
    }



    //GETTERS
    
    //view significa que nao tem transacao, nao precisa minerar (nao usa gas para executar)
    
    function getStatus() public view returns (Status) {
        return status;
    }

    function getClient() public view returns (string memory) {
        return client;
    }
    
    function getCreationDate() public view returns (int) {
        return creationDate;
    }

    function getActivationDate() public view returns (int) {
        return activationDate;
    }

    function getTerminationDate() public view returns (int) {
        return terminationDate;
    }

    function getOblig1() public view returns (Oblig memory) {
        return oblig1;
    }

    function getOblig2() public view returns (Oblig memory) {
        return oblig2;
    }

    function getOblig3() public view returns (Oblig memory) {
        return oblig3;
    }

    function getOblig4() public view returns (Oblig memory) {
        return oblig4;
    }

    function getOblig5() public view returns (Oblig memory) {
        return oblig5;
    }

    function getOblig6() public view returns (Oblig memory) {
        return oblig6;
    }

    function getOblig7() public view returns (Oblig memory) {
        return oblig7;
    }

    // Retorna apenas o status de uma obrigação (1..7).
    function getObligStatus(uint8 number) public view returns (ObligStatus) {
        if (number == 1) { return oblig1.status; }
        else if (number == 2) { return oblig2.status; }
        else if (number == 3) { return oblig3.status; }
        else if (number == 4) { return oblig4.status; }
        else if (number == 5) { return oblig5.status; }
        else if (number == 6) { return oblig6.status; }
        else if (number == 7) { return oblig7.status; }
        revert(unicode"Obrigação inexistente (use 1..7)");
    }

    

}