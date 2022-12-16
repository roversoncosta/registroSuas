from app.models import User
import pandas as pd

def bulk_create_users():
    df = pd.read_csv('users.csv')
    df_records = df.to_dict('records')
    model_instances = [User(
        username = record['username'],
        first_name =record['first_name'],
        last_name = record['last_name'],
        email = record['email'],
        password = record['password1'],
        # password2 = record['password2'],
        sector_name = record['sector_name']
        )  for record in df_records ]
    User.objects.bulk_create(model_instances)
    # AcaoAtpModel.objects.filter(user_id=1).delete()
    # ## Insert data into Model
    # # Para rodar um codigo python usando o shell: python manage.py shell <importing.py
bulk_create_users()