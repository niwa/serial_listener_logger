from sell import SerialListenerLogger

def test_fake_call_serial():
    '''
    make sure call serial is working
    '''
    logger = SerialListenerLogger()

    assert logger != None, 'Failed to create logger'
