def detect_layout_type(filename):

    name = filename.lower()

    if "login" in name:
        return "login"
    if "dashboard" in name:
        return "dashboard"
    if "form" in name:
        return "form"
    if "profile" in name:
        return "profile"

    return "dashboard"


def generate_code(framework, layout_type, existing_components):

    component_name = "GeneratedScreen"
    if existing_components:
        component_name = existing_components[0]

    if framework == "React":
        return generate_react(component_name, layout_type)

    if framework == "Vue.js":
        return generate_vue(component_name, layout_type)

    if framework == "Angular":
        return generate_angular(layout_type)

    return "// Unsupported framework"


def generate_react(name, layout):

    if layout == "login":
        return f"""
import React from 'react';

export default function {name}() {{
  return (
    <div style={{display:"flex",justifyContent:"center",alignItems:"center",height:"100vh"}}>
      <div style={{padding:"40px",border:"1px solid #ddd",borderRadius:"8px"}}>
        <h2>Login</h2>
        <input placeholder="Email" style={{display:"block",marginBottom:"10px"}} />
        <input placeholder="Password" type="password" style={{display:"block",marginBottom:"10px"}} />
        <button>Login</button>
      </div>
    </div>
  );
}}
"""

    if layout == "form":
        return f"""
import React from 'react';

export default function {name}() {{
  return (
    <div style={{padding:"40px"}}>
      <h2>Contact Form</h2>
      <input placeholder="Name" />
      <input placeholder="Email" />
      <textarea placeholder="Message"></textarea>
      <button>Submit</button>
    </div>
  );
}}
"""

    return f"""
import React from 'react';

export default function {name}() {{
  return (
    <div style={{padding:"30px"}}>
      <h1>Dashboard</h1>
      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:"20px"}}>
        <div style={{padding:"20px",border:"1px solid #ddd"}}>
          <h3>Analytics</h3>
          <p>Visitors: 1,245</p>
        </div>
        <div style={{padding:"20px",border:"1px solid #ddd"}}>
          <h3>Reports</h3>
          <p>Monthly Growth: 12%</p>
        </div>
      </div>
    </div>
  );
}}
"""


def generate_vue(name, layout):
    return f"""
<template>
  <div class="container">
    <h1>{layout.capitalize()} Screen</h1>
    <p>Generated using Smart Simulation Mode</p>
  </div>
</template>

<script>
export default {{
  name: "{name}"
}}
</script>

<style scoped>
.container {{ padding: 30px; }}
</style>
"""


def generate_angular(layout):
    return f"""
<div class="container">
  <h1>{layout.capitalize()} Screen</h1>
  <p>Generated using Smart Simulation Mode</p>
</div>
"""
