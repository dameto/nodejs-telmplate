import os

path = input("Project Path: ")
pName = input("Project Name (Without Spaces!): ")
version = input("Project Version: ")
name = input("Author Name: ")

# Acces Path
os.chdir(path)

# Make Project Folder
os.system('cmd /c "mkdir ' + pName + '"')

# Access Project Folder
os.chdir('./' + pName)

# >>npm init
os.system('cmd /c "npm config ls -l"')
os.system('cmd /c "npm config set init-author-name "' + name + '" -g"')
os.system('cmd /c "npm config set init-version "' + version + '" -g"')
os.system('cmd /c "npm config set init-main "server.js" -g"')
os.system('cmd /c "npm init -y"')

# Install Default Modules
os.system('cmd /c "npm i ejs"')
os.system('cmd /c "npm i express"')

# Make Default Need Folders---

# Make "routes" Folder
os.system('cmd /c "mkdir routes"')
# Make "models" Folder
os.system('cmd /c "mkdir models"')


# Create server.js
os.system('cmd /c "echo //Modules > server.js"')
with open('server.js', 'a+') as f:
    f.write('const express = require("express")\n'
            'const ejs = require("ejs")\n\n'

            'const app = express()\n\n'

            '//Use\n'
            'app.use(express.urlencoded({ extended: false }))\n\n'

            '//Get Public Folder\n'
            'app.use(express.static(__dirname + "/public/"))\n\n'

            '//Creating Server\n'
            'app.use(express.json())\n'
            'app.set("view engine", "ejs")\n'
            'const port = process.env.PORT || 7777\n\n'

            '//Listen Port\n'
            'app.listen(port, () => console.log(`Listening - Port: ${port}`));\n\n'

            '//Home Route\n'
            'app.get("/", (req, res) => {\n'
            '   res.render("index.ejs")\n'
            '})')
f.close()


# PUBLIC-------------------------
# Make and access "public" Folder
os.system('cmd /c "mkdir public"')
os.chdir('./public')
# Make folders in "public"
# img
os.system('cmd /c "mkdir img"')
# js
os.system('cmd /c "mkdir js"')
os.chdir('./js/')
os.system('cmd /c "echo //... > script.js"')
# css
os.chdir('../')
os.system('cmd /c "mkdir css"')
os.chdir('./css')
os.system('cmd /c "echo *{} > master.scss"')


# VIEWS--------------------------
os.system('cmd /c "mkdir views"')
