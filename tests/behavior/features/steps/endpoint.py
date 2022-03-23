from behave import when, then
from requests import post
from json import loads

@when('enviar o json')
def request_api_id_title(context):
    context.api_requests = post(context.base_url + '/validate-json',json=loads(context.text))

    #raise NotImplementedError('STEP: When enviar o json')

@then('a API deve retornar {status_code:d}')
def check_api_right(context, status_code):
    assert context.api_requests.status_code == status_code #raise NotImplementedError('STEP: Then a API deve retornar 201')
