import django_basic_crud_generator

model_name = str(input("Nom du modele a generer: "))

django_basic_crud_generator.generate_files(
    app_name="appli",
    model_name = model_name,
    use_template_layout=True
)