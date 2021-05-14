*** Settings ***
Library     Remote  ${SERVER}:${PORT}    WITH NAME      keyboardDevice

*** Variables ***
${SERVER}   192.168.0.114
${PORT}     8270

*** Test Cases ***
Send String
    keyboardDevice.Send String     TEST