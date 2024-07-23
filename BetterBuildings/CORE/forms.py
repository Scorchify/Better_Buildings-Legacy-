from django import forms

class InputBox(forms.Textarea):
    class Media:
        css = {
            "all": ["css/input.css"],  
        }

class loginHSForm(forms.Form):
    class Media:
        css = {
            "all": ["css/input.css"]
        }
    
    school = forms.ChoiceField(
        choices=[
            ('', 'Select'),  # Default option
            ('BethesdaChevyChaseHS', 'Bethesda-Chevy Chase'),
            ('MontgomeryBlairHS', 'Montgomery Blair'),
            ('JamesHubertBlakeHS', 'James Hubert Blake'),
            ('WinstonChurchillHS', 'Winston Churchill'),
            ('ClarksburgHS', 'Clarksburg'),
            ('DamascusHS', 'Damascus'),
            ('AlbertEinsteinHS', 'Albert Einstein'),
            ('GaithersburgHS', 'Gaithersburg'),
            ('WalterJohnsonHS', 'Walter Johnson'),
            ('JohnFKennedyHS', 'John F. Kennedy'),
            ('ColZadokMagruderHS', 'Col. Zadok Magruder'),
            ('RichardMontgomeryHS', 'Richard Montgomery'),
            ('NorthwestHS', 'Northwest'),
            ('NorthwoodHS', 'Northwood'),
            ('PaintBranchHS', 'Paint Branch'),
            ('PoolesvilleHS', 'Poolesville'),
            ('QuinceOrchardHS', 'Quince Orchard'),
            ('RockvilleHS', 'Rockville'),
            ('SenecaValleyHS', 'Seneca Valley'),
            ('SherwoodHS', 'Sherwood'),
            ('SpringbrookHS', 'Springbrook'),
            ('WatkinsMillHS', 'Watkins Mill'),
            ('WheatonHS', 'Wheaton'),
            ('WaltWhitmanHS', 'Walt Whitman'),
            ('ThomasSWoottonHS', 'Thomas S. Wootton'),
        ],
        widget=forms.Select(attrs={
            "class": "select",
        }),
        label="Select Your School"
    )

    def clean_school(self):
        data = self.cleaned_data['school']
        if data == '':
            raise forms.ValidationError("Please select a valid option.")
        return data
    
class loginMSForm(forms.Form):
    class Media:
        css = {
            "all": ["css/input.css"]
        }
    
    school = forms.ChoiceField(
        choices=[
            ('', 'Select'),  # Default option
            ('ArgyleMS', 'Argyle'),
            ('JohnTBakerMS', 'John T. Baker'),
            ('BenjaminBannekerMS', 'Benjamin Banneker'),
            ('BriggsChaneyMS', 'Briggs Chaney'),
            ('CabinJohnMS', 'Cabin John'),
            ('RobertoWClementeMS', 'Roberto W. Clemente'),
            ('EasternMS', 'Eastern MS'),
            ('WilliamHFarquharMS', 'William H. Farquhar'),
            ('ForestOakMS', 'Forest Oak'),
            ('RobertFrostMS', 'Robert Frost'),
            ('GaithersburgMS', 'Gaithersburg'),
            ('HerbertHooverMS', 'Herbert Hoover'),
            ('FrancisScottKeyMS', 'Francis Scott Key'),
            ('DrMartinLutherKingJrMS', 'Dr. Martin Luther King, Jr.'),
            ('KingsviewMS', 'Kingsview'),
            ('LakelandsParkMS', 'Lakelands Park'),
            ('AMarioLoiedermanMS', 'A. Mario Loiederman'),
            ('MontgomeryVillageMS', 'Montgomery Village'),
            ('NeelsvilleMS', 'Neelsville'),
            ('NewportMillMS', 'Newport Mill'),
            ('NorthBethesdaMS', 'North Bethesda'),
            ('ParklandMS', 'Parkland'),
            ('RosaMParksMS', 'Rosa M. Parks'),
            ('JohnPooleMS', 'John Poole'),
            ('ThomasWPyleMS', 'Thomas W. Pyle'),
            ('RedlandMS', 'Redland'),
            ('RidgeviewMS', 'Ridgeview'),
            ('RockyHillMS', 'Rocky Hill'),
            ('ShadyGroveMS', 'Shady Grove'),
            ('OdessaShannonMS', 'Odessa Shannon'),
            ('SilverCreekMS', 'Silver Creek'),
            ('SilverSpringIntlMS', 'Silver Spring Intl'),
            ('SligoMS', 'Sligo'),
            ('TakomaParkMS', 'Takoma Park'),
            ('TildenMS', 'Tilden'),
            ('HallieWellsMS', 'Hallie Wells'),
            ('JuliusWestMS', 'Julius West'),
            ('WestlandMS', 'Westland'),
            ('WhiteOakMS', 'White Oak'),
            ('EarleBWoodMS', 'Earle B. Wood'),
        ],
        widget=forms.Select(attrs={
            "class": "select",
        }),
        label="Select Your School"
    )

    def clean_q2(self):
        data = self.cleaned_data['school']
        if data == '':
            raise forms.ValidationError("Please select a valid option.")
        return data
  
    

class LoginForm(forms.Form): # not used
    class Media:
        css = {
            "all": ["css/login.css"]
        }
    Name = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Name (First and Last)",
            "class": "input-box",
            "autocomplete": "off",
            "rows": 2,
            "cols": 25
        }),
        label=''
    )
    School = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "School",
            "class": "input-box",
            "autocomplete": "off",
            "rows": 2,
            "cols": 25
        }),
        label=''
    )

    

class ReportingForm(forms.Form):
    q1 = forms.CharField(
        widget=InputBox(attrs={
            "placeholder": "Enter your response here!",
            "class": "input-box",
            "rows": 4,  
            "cols": 50  
        }),
        label=''
    )
    q2 = forms.ChoiceField(
        choices=[
            ('', 'Select'),  # Default option
            ('Bathrooms', 'Bathrooms'),
            ('Building', 'Building'),
            ('Other', 'Other')
        ],
        widget=forms.Select(attrs={
            "class": "select",
        }),
        label="How would you categorize your issue?"
    )

    def clean_q2(self):
        data = self.cleaned_data['q2']
        if data == '':
            raise forms.ValidationError("Please select a valid option.")
        return data

