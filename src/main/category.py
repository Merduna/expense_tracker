class Category():
    category_tree = [[]]
    root_initialized = False
    categories = []

    @classmethod
    def initialize_root(cls):
        root_instance = cls.__new__(cls)
        root_instance._Category__name = 'Root Category'
        root_instance._Category__level = 0
        root_instance._Category__parent = None
        root_instance._Category__subcategories = []
        root_instance._Category__category_id = root_instance._Category__generate_category_id()
        
        cls.category_tree[0].append(root_instance)
        
        cls.root_initialized = True
        

    def __init__(self, name, parent=None):
        self.__level = 0
        self.__name = name
        self.__parent = parent
        self.__subcategories = []

        if not Category.root_initialized:
            Category.initialize_root()
        if not parent:
            self.__parent = Category.category_tree[0][0]           
        
        if self.__parent:
            self.__level = self.__parent.get_level() + 1
            self.__add_to_category_tree()
            self.__parent.add_subcategory(self)

        self.__category_id = self.__generate_category_id()     
        Category.categories.append(self)

    def __str__(self):
        return "\n\nlevel: " + str(self.get_level()) + "\ncategory_id: " + str(self.get_category_id()) + "\nname: " + str(self.get_name()) + "\nparent: " + (('id '  + str(self.get_parent().get_category_id()) + ' | lvl ' + str(self.get_parent().get_level()) + ' | name '+ self.get_parent().get_name()) if self.get_parent() != None else "") + "\nsubcategories:" + str(self.get_subcategories())

    def get_path(self, names=False):
        if names:
            if self.get_parent():
                return self.get_parent().get_path(True) + [self.get_name()]
            else:
                return [self.get_name()]
        else:
            if self.get_parent():
                return self.get_parent().get_path() + [self.get_parent().get_subcategories().index(self) + 1]
            else:
                return [1]


    def write_tree(self, depth=0):
        result = f"{depth};{self.get_name()};{tuple(self.get_path())}\n"
        for child in self.get_subcategories():
            if child != None:
                result += child.write_tree(depth + 1)
        return result
    
    @classmethod
    def write_all_trees(cls):
        result = ""
        for category in cls.categories:
            if not category.get_parent():
                result += category.write_tree()
        return result


    def __add_to_category_tree(self):           
        if len(Category.category_tree) == self.get_level():
            Category.category_tree.append([])
        Category.category_tree[self.get_level()].append(self)

    def __generate_category_id(self):
        id_list = [1]
        current_level = self
        while current_level.get_level() != 0:
            count = 0
            for category in Category.category_tree[current_level.get_level()]:
                if category.get_parent() == current_level.get_parent():
                    count += 1
                if category is current_level:
                    break
            id_list.insert(1, count)
            current_level = current_level.get_parent()
        return tuple(id_list)

    def __set_category_id(self, category_id):
        self.__category_id = category_id

    def delete(self):
        try:
            assert len(self.__subcategories) == 0
            if self.__parent:
                self.__parent.get_subcategories()[self.__parent.get_subcategories().index(self)] = None
                Category.category_tree[self.get_level()][Category.category_tree[self.get_level()].index(self)] = None
        except AssertionError:
            print('Can\'t delete a category that has subcategories.\n' + self.get_name(), 'has the following subcategories:')
            for subcategory in self.__subcategories:
                print(subcategory.get_category_id(), ':', subcategory.get_name())
    
    def get_level(self):
        return self.__level

    def __set_level(self, level):
        self.__level = level
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_category_id(self):
        return self.__category_id
    
    def get_parent(self):
        return self.__parent
    
    def set_parent(self, new_parent):
        if self.__parent is not None and new_parent != self.__parent:
            self.__parent.get_subcategories().remove(self)

        self.__parent = new_parent

        if new_parent is not None and self not in new_parent.get_subcategories():
            new_parent.get_subcategories().append(self)

    def get_subcategories(self):
        return self.__subcategories
    
    def add_subcategory(self, subcategory):
        self.__subcategories.append(subcategory)        
    
    def print_tree(root=0, recursion=0):
        recursion = recursion + 1
        if root == 0:
            root = Category.category_tree[0][0]
            print('\n--- Category Tree ---\n')
            print(root.get_category_id(), root.get_name())
        for branch in root.get_subcategories():
            if recursion > 10:
                break
            if branch:
                print('\t' * (len(branch.get_category_id()) - 1), branch.get_category_id(), branch.get_name())
                Category.print_tree(branch, recursion)


    def exp_categories(filename):
        try:
            assert filename.isalnum()
            f = open(filename + '.csv', 'w')
            f.write(Category.write_all_trees())
            f.close()
        except AssertionError:
            print('Invalid filename. Please enter only letters and numbers.')
        except:
            print('The operation didn\'t work')


    def imp_categories(filename):
        try:
            assert filename.isalnum()
            f = open(filename + '.csv', 'r')
            data = f.readlines()
            f.close()
            return data
        except:
            print('The operation didn\'t work')


    @classmethod
    def load_categories(cls, data):
        cls.categories = []
        cls.category_tree = [[]]
        cls.initialize_root()

        def get_or_create_category_by_id(category_id, name=None, parent=None):
            for level in Category.category_tree:
                for category in level:
                    if category and category.get_category_id() == category_id:
                        if parent:
                            category.set_parent(parent)
                        return category
            return cls(name, parent)

        for line in data:
            parts = line.strip().split(';')
            depth = int(parts[0])
            name = parts[1]

            path_str = parts[2][1:-1].strip()
            path = tuple(map(int, filter(None, path_str.split(','))))

            # print("current name: ", name, 'current id: ', path)
            current_category = Category(name)
            current_category.__set_category_id(path)
            current_category.__set_level(depth)            
            if depth == 0:
                parent = None
            else:
                parent = get_or_create_category_by_id(path[:-1])

            current_category.set_parent(parent)
            #print(str(current_category))