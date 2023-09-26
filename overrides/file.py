import frappe
    
ALLOWED_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.mp3','.wav']
DISALLOWED_EXTENSIONS = ['.exe', '.php','.py','.js']

def write_file(*args, **kwargs):
    # print('writing file now............................')

    # print('ARGS')
    # for arg in args:
    #     print(f'args: {arg}, type: {type(arg)}')
    
    # print(f'file name: {args[0].file_name}')

    # print('KWARGS:')
    # for k, v in kwargs.items():
    #     print(f'{k} : {v}')

    # args[0].save_file_on_filesystem()

    file = args[0]
    fileName = file.file_name
    errMessage = 'Only ' + ', '.join(ALLOWED_EXTENSIONS) + ' files are allowed!'

    if any([ext in fileName for ext in DISALLOWED_EXTENSIONS]) or all([ext not in fileName for ext in ALLOWED_EXTENSIONS]):
        frappe.throw(errMessage)
        return
    
    file.save_file_on_filesystem()
    
