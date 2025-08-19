# dsa-code-practices
code practices of strivers dsa

 1. Build a Strong Foundation
- HTML & CSS: Master layouts, forms, Flexbox, Grid, and responsive design.
- JavaScript: Deepen your understanding of ES6+, DOM manipulation, closures, hoisting, and event loops (you’re already on the right track!).
🛠️ Practice: Recreate simple websites like a portfolio page or a product landing page.

⚛️ 2. React Mastery
- Learn React fundamentals: components, props, state, and hooks (useState, useEffect).
- Build small apps: to-do list, weather app, or a quiz app.
- Explore React Router and basic state management.
🧪 Challenge: Convert a static HTML page into a dynamic React app.

🧠 3. Problem-Solving & Aptitude
- Practice coding challenges daily on platforms like LeetCode, CodeSignal, or HackerRank.
- Focus on arrays, strings, recursion, and object manipulation in JavaScript.
🧩 Tip: Time yourself to simulate interview pressure.

🧰 4. Tools of the Trade
- Git & GitHub: Learn version control and how to collaborate on projects.
- VS Code: Get comfortable with extensions, debugging, and shortcuts.
- Browser DevTools: Inspect elements, debug JS, and analyze performance.

📚 5. Learn by Doing
- Contribute to open-source or clone real-world apps (like a mini YouTube or Instagram).
- Document your learning on GitHub or a blog—it shows initiative and helps retention.

🎯 6. Interview Prep
- Practice behavioral questions and project explanations.
- Prepare for aptitude tests and technical rounds with mock interviews.





Mounting
Mounting is the phase when a component is inserted into the DOM for the first time. It includes:
- Creating the component instance
- Calling lifecycle methods like constructor, render, and componentDidMount
- Actually placing the component’s output into the DOM
Think of it as React saying, “Hey, this component is new—let’s build and display it.”
🔁 Rendering
Rendering is the process of generating the virtual DOM from your component’s JSX. It happens:
- During the initial mount
- Every time props or state change (i.e., during updates)
So rendering can happen multiple times, but mounting happens only once per component instance.
