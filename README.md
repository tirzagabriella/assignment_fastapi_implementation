# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Table of contents

- [Overview](#overview)

  - [The challenge](#the-challenge)

- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Docker](#docker)
  - [Useful resources](#useful-resources)
- [Author](#author)
- [Link](#link)

## Overview

### The challenge

Users should be able to:

- View the optimal layout for the app depending on their device's screen size
- Adding a new piece of list using add function
- click/un-click list button (complete/incomplete statement)
- choose datetime for deadline
- implemented useeffect to update list based on filter value
- added functionality to edit existing task (only the name of the task)
- Select filter (all, incomplete, complete)

## My process

- Build React JSX Structure
- Use CSS and tailwind for Styling
- Use libraries for some components
- Use routing library
- Implemented datetime picker using MUI X
- Implemented local-storage

### Built with

- React JSX
- CSS and Tailwind
- Vite
- MUI X

### What I learned

- Using React JSX for structuring

- How to use routing to change pages

- Use react state (like "filtering" in this case)

- Styling using tailwind

### Docker

- install docker desktop

- install docker CLI

- create Dockerfile

- create docker image : docker build . -t "todolist-assignment:v1.0"

- to run image in the background (inside a container) : docker run -d -p 5173:5173 todolist-assignment:v1.0

- to change the tag (we'll need this especially when using dockerhub, in order to match the user at dockerhub at the repo) : docker tag todolist-assignment:v1.0 tirzagabriella20/todolist-assignment:v1.0

- to push to dockerhub : docker push tirzagabriella20/todolist-assignment:v1.0

### Useful resources

- [Tailwind](https://devpress.csdn.net/react/62ec1e2789d9027116a1033f.html) - This helped me to make pop up function and using tailwind
- [Routing](https://reactrouter.com/en/main/hooks/use-navigate) - This is an amazing article which helped me finally understand how to use Routing.
- [ColorPallete](https://colorhunt.co/palette/944e63b47b84caa6a6ffe7e7) - I use this for my color pallete
- [Datetime](https://mui.com/x/react-date-pickers/adapters-locale/) - I use this to implement datetime picker using MUI X

## Author

Tirza Gabriella (2602109870)
Computer Science Student at Binus University

## Link

https://to-do-list-assignment2-74avki8qu-tirzagabriellas-projects.vercel.app
