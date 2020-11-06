import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for file_name in files:
                local_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.AlAxfJtvmMiCNMLKod7gOmYbfZkzx87EOf8tOKovAURiOGmdqogxd-puay0hlDkMQnF1u2eNWFYUS5VCzUoFCi_mgeH2KBfXAeRbc9IVj_GyA0jlqHtv0RqwlnGtzwlwd3mhf59-UIk'
    transfer_data = TransferData(access_token)

    file_from = str(input("Enter the file path to transfer: "))
    file_to = input("Enter the full path to upload to dropbox: ")

    transfer_data.upload_file(file_from, file_to) 
    print("Files uploaded successfully")

main()