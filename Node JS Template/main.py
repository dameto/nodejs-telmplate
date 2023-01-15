import os

path = input("Project Path: ")
pName = input("Project Name (Without Spaces!): ")
version = input("Project Version: ")
name = input("Author Name: ")

# Acces Path
os.chdir(path)

# Make Project Folder
os.mkdir(pName)

# Access Project Folder
os.chdir('./' + pName)




##################################
########## ---SERVER--- ##########
##################################

os.mkdir('server')
os.chdir('./server')

# >>npm init
os.system('cmd /c "npm config ls -l"')
os.system('cmd /c "npm config set init-author-name "' + name + '" -g"')
os.system('cmd /c "npm config set init-version "' + version + '" -g"')
os.system('cmd /c "npm config set entry-point "app.js" -g"')
os.system('cmd /c "npm config set test-command "nodemon" -g"')
os.system('cmd /c "npm init -y"')

# modify package.json
os.remove('package.json')
with open('package.json', 'w') as fp:
    fp.write(
        '{\n'
            '\t"name": "server",\n'
            '\t"version": "1.0.0",\n'
            '\t"description": "",\n'
            '\t"main": "app.js",\n'
            '\t"scripts": {\n'
                '\t\t"dev": "nodemon"\n'
            '\t},\n'
            '\t"keywords": [],\n'
            '\t"author": "",\n'
            '\t"license": "ISC",\n'
            '\t"dependencies": {\n'
                '\t\t"cors": "^2.8.5",\n'
                '\t\t"express": "^4.18.2"\n'
            '\t}\n'
        '}'
    )


# Make Default Folders
os.mkdir('routes')
os.mkdir('models')
os.mkdir('middleware')

# Install Default Modules
os.system('cmd /c "npm i express cors"')

# Files
# Create app.js
with open('app.js', 'w') as fp:
    fp.write(
        'const express = require("express")\n'
        'const cors = require("cors")\n'
        'const express = require("express")\n'
        '// const { MONGOURI } = require("./keys")\n\n'
        
        'const app = express()\n'
        'app.use(cors())\n'
        'app.use(express.json())\n\n'   
        
        '/* ----------------------- */\n' 
        '/* -----CONFIGURATION----- */\n'
        '/* ----------------------- */\n\n'

        '// Database\n'
        '/* mongoose.set("strictQuery", true);\n'
        'mongoose.connect(MONGOURI, () => {console.log("Database Connection Acquired")}, {\n'
            '\tuseNewUrlParser: true,\n'
            '\tuseUnifiedTopology: true\n'
        '})*/\n'
        '// Models\n\n'

        '// Routers\n\n'

        '// Get Public Folder\n'
        'app.use(express.static(__dirname + "/public/"))\n\n'

        '// Creating Server\n'
        'const port = process.env.PORT || 8000\n'
        'app.listen(port, () => console.log(`Listening - Port: ${port}`));\n\n'
    )
# Create keys.js
with open('keys.js', 'w') as fp:
    fp.write(
        '/* module.exports={\n'
            '\tMONGOURI: {key}\n'
        '} */\n'
    )
# Create .gitignore
with open('.gitignore', 'w') as fp:
    fp.write(
        'node_modules'
    )


##################################
########## ---CLIENT--- ##########
##################################

os.chdir('../')
os.system('cmd /c "npm create vite@latest client -- --template react"')
os.chdir('./client')
os.system('cmd /c "npm install"')

os.system('cmd /c "npm i react-router-dom axios"')
os.system('cmd /c "npm install -D tailwindcss postcss autoprefixer"')
os.system('cmd /c "npx tailwindcss init -p"')

# modify tailwind.config.cjs
os.remove('tailwind.config.cjs')
with open('tailwind.config.cjs', 'w') as fp:
    fp.write(
        '/** @type {import("tailwindcss").Config} */\n'
        'module.exports = {\n'
            '\tcontent: [\n'
                '\t\t"./index.html",\n'
                '\t\t"./src/**/*.{js,ts,jsx,tsx}",\n'
            '\t],\n'
            '\ttheme: {\n'
                '\t\textend: {},\n'
            '\t},\n'
            '\tplugins: [],\n'
        '}\n'
    )



# Make Default Folders
os.chdir('./src')
os.mkdir('routes')
os.mkdir('components')



# -Modify src files-
# delete App.css
os.remove('App.css')

# modify index.css
os.remove('index.css')
with open('index.css', 'w') as fp:
    fp.write(
        '@tailwind base;\n'
        '@tailwind components;\n'
        '@tailwind utilities;\n\n'

        '* {\n'
        '\toutline: none;\n'
        '}\n'
    )

# modify main.jsx
os.remove('main.jsx')
with open('main.jsx', 'w') as fp:
    fp.write(
        "import React from 'react'\n"
        "import ReactDOM from 'react-dom/client'\n"
        "import App from './App'\n"
        "import './index.css'\n"
        "import { BrowserRouter } from 'react-router-dom';\n\n"

        "ReactDOM.createRoot(document.getElementById('root')).render(\n"
            "\t<React.StrictMode>\n"
                "\t\t<BrowserRouter>\n"
                    "\t\t\t<App />\n"
                "\t\t</BrowserRouter>\n"
            "\t</React.StrictMode>,\n"
        ")\n"
    )

# modify App.jsx
os.remove('App.jsx')
with open('App.jsx', 'w') as fp:
    fp.write(
        "import { useState } from 'react'\n"
        "import { Routes, Route } from 'react-router-dom';\n\n"

        "// Components\n\n"

        "// Routes\n"
        "import Home from './routes/Home';\n\n"

        "function App() {\n"
            "\treturn (\n"
                "\t\t<>\n"
                    "\t\t\t<Routes>\n"
                        "\t\t\t\t<Route path='/' element={<Home />} />\n"
                    "\t\t\t</Routes>\n"
                "\t\t</>\n"
            "\t)\n"
        "}\n\n"

        "export default App\n"
    )

# create axios.js
with open('axios.js', 'w') as fp:
    fp.write(
        'import axios from "axios";\n\n'

        'const instance = axios.create({\n'
            '\tbaseURL: "http://localhost:8000/"\n'
        '})\n\n'

        'export default instance;\n'
    )



# Home Route
os.chdir('./routes')
with open('Home.jsx', 'w') as fp:
    fp.write(
        "import { useState } from 'react'\n\n"

        "// Components\n\n"

        "export default function Home() {\n"
            "\treturn (\n"
                "\t\t<section className='flex items-start justify-center'>\n"
                    "\t\t\t<h1>Home</h1>\n"
                "\t\t</section>\n"
            "\t)\n"
        "}\n"
    )



# Assets cleanup
os.chdir('../assets')
os.remove('react.svg')

# Public cleanup
os.chdir('../../public')
os.remove('vite.svg')

