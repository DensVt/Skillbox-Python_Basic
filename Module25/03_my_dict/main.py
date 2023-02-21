class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


new_dict = MyDict()
new_dict["Inary"] = 12
new_dict["Inno"] = 14
new_dict["Temary"] = 18
print(new_dict)
print(f"Возвращает - {new_dict.get('Lee')}")
