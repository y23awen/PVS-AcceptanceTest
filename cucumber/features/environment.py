# # from selenium import webdriver


# # def before_feature(context, feature):
# #     model.init(environment='test')
# #     if 'browser' in feature.tags:
# #         context.server = simple_server.WSGIServer(('', 8000))
# #         context.server.set_app(web_app.main(environment='test'))
# #         context.thread = threading.Thread(target=context.server.serve_forever)
# #         context.thread.start()
# #         context.browser = webdriver.Chrome()

# # def after_feature(context, feature):
# #     if 'browser' in feature.tags:
# #         context.server.shutdown()
# #         context.thread.join()
# #         context.browser.quit()

# from selenium import webdriver

# def before_scenario(context, scenario):
# 	driver = webdriver.Chrome()
# 	# desired_capabilities['version'] = 'latest'
# 	# desired_capabilities['platform'] = 'WINDOWS'
# 	# desired_capabilities['name'] = 'Testing Selenium with Behave'
# 	# desired_capabilities['client_key'] = 'key'
# 	# desired_capabilities['client_secret'] = 'secret'

    
# 	context.browser = webdriver.Remote(
# 		command_executor="http://localhost:3001"
# 	)

# def after_scenario(context, scenario):
# 	context.browser.quit()

#     # driver = webdriver.Remote(
#     # command_executor='http://localhost:3001',
#     # desired_capabilities=desired_caps)