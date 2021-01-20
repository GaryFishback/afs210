import enum
# Using enum class create enumerations
class Countries(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

for data in Countries:
    print(f'{data.name} = {data.value}' )