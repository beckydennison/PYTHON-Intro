class Rectangle(object):

    def __init__(self, height = 1, width = 2):
      self.height = height
      self.width = width
      
    def set_height(self, customHeight):
        self.height = customHeight

    def set_width(self, customWidth):
        self.width = customWidth

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (self.height*2) + (self.width*2)
        


my_rect = Rectangle(40,4)

print('The length is',my_rect.get_height())
print('The width is', my_rect.get_width())
print('The perimeter is', my_rect.get_perimeter())
print('The area is',my_rect.get_area())


my_rect = Rectangle(35.7,3.5)

print('The length is',my_rect.get_height())
print('The width is', my_rect.get_width())
print('The perimeter is', my_rect.get_perimeter())
print('The area is',my_rect.get_area())

input('press enter to continue')

