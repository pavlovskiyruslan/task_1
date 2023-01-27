import requests

response = requests.get("https://reqres.in/api/users?page=2")
print("LIST_USERS")
print(response.status_code)
assert response.status_code == 200
print(response.text)

print("\n")
print("SINGLE_USER")
single_user = requests.get("https://reqres.in/api/users/2")
print(single_user.status_code)
print(single_user.text)
assert single_user.status_code == 200

single_user_error = requests.get("https://reqres.in/api/users/999")
print(single_user_error.status_code)
print(single_user_error.json())
assert single_user.status_code == 200

print("\n")
print("CREATE_USER")
create_user = requests.post("https://reqres.in/api/users", json={
    "name": "morpheus",
    "job": "leader"
})
print(create_user.status_code)
print(create_user.text)
print("FINISHED")
assert create_user.status_code == 201


print("////////////////////////////////////////////////////////////////////\n")



print("\n")
print("PUT_USER")
put_user = requests.put("https://reqres.in/api/users/2",json = {
    "name": "morpheus",
    "job": "zion resident"
})
print(put_user.status_code)
print(put_user.text)
#assert response.json().get('name') == 'morpheus'
assert single_user.status_code == 200
print("////////////////////////////////////////////////////////////////////\n")


print("\n")
print("PATCH_USER")
patch_user = requests.patch("https://reqres.in/api/users/2", json={
    "name": "morpheus",
    "job": "zion resident"
})
print(patch_user.status_code)
print(patch_user.json())
#assert response.json().get('name') == 'morpheus'
assert patch_user.status_code == 200
print("////////////////////////////////////////////////////////////////////\n")


print("\n")
print("DELETE")
delete_req = requests.delete("https://reqres.in/api/users/2")
print(delete_req.status_code)
print(delete_req.text)
assert delete_req.status_code == 204
print("////////////////////////////////////////////////////////////////////\n")







