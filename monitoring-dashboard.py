from flask import Flask, jsonify

app = Flask(__name__)

# Example agent status (stub)
agent_status = {
    "Agent1": "Running",
    "Agent2": "Idle"
}

@app.route('/status')
def status():
    return jsonify(agent_status)

@app.route('/start_agent/<agent_name>')
def start_agent(agent_name):
    # Logic to start agent
    agent_status[agent_name] = "Running"
    return jsonify({"message": f"Agent {agent_name} started"})

@app.route('/stop_agent/<agent_name>')
def stop_agent(agent_name):
    # Logic to stop agent
    agent_status[agent_name] = "Stopped"
    return jsonify({"message": f"Agent {agent_name} stopped"})

if __name__ == '__main__':
    app.run(debug=True)
