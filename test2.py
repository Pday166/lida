import google.generativeai as palm

palm.configure(api_key="PALM_API_KEY")
models = palm.list_models()
print("Available models:")
for model in models:
    print(model.name)

