def errorResponse(key):
    dic_Response={
        '100':'Continure',
        '101':'Switch Protocol'
        '200':'Success'
        '201':'Have been Build'
    }
    str_Response='Error '+key+' : '+dic_Response[key]
    return str_Response