import requests

registered_triggers = []

# Builder function
def make_login_agent(config):

    # Login modules pf tje 
    @time_trigger(f"period(now, {config['interval']})")
    def cuhk_resnet_login():
        task.unique("CUHK_RESNET_LOGIN")

        login_url = config['url']
        input_data = {'user' : config['uid'] , 'password' : config['upw'] , 'cmd' : 'authenticate' , 'Login' : 'Log+In'}
        
        # Send the request
        try:
            r = task.executor(requests.post, login_url, input_data, allow_redirects=False)
        except Exception:
            log.error(f"Request has some error")

        if 'Welcome' in r.text:
            log.info("ResNet Login Success")
        else: 
            if r.status_code == 302:
                log.info("Login NOT yet timeout")
            else:
                log.warning("Login ERROR")
                log.warning("Code: " + str(r.status_code))

    registered_triggers.append(cuhk_resnet_login)

# Run the Builder function on startup
@time_trigger('startup')
def cuhk_resnet_login_startup():
    for app in pyscript.app_config:
        make_login_agent(app) 