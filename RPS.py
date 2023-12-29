def player(prev_play, opponent_history=[]):
  opponent_history.append(prev_play)

  # Define ideal responses
  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

  # Respond based on opponent's recent moves
  if len(opponent_history) >= 4:
      last_four = "".join(opponent_history[-4:])
      # Check for opponent's repeated moves
      if last_four.count(last_four[0]) == 4:
          return ideal_response[last_four[0]]

      # Check for specific patterns against Abbey
      pattern_responses_abbey = {
          "PRSR": "S",
          "SRRP": "P",
          "RSRS": "P",
          "SSRP": "R",
          "SSSS": "R",
          "SSPP": "P",  # New response for Abbey's repetitive pattern
      }
      if last_four in pattern_responses_abbey:
          return pattern_responses_abbey[last_four]

      # Check for specific patterns against Kris
      pattern_responses_kris = {
          "RPSR": "P",
          "SPPP": "R",
          "RPRP": "S",
          "RSPP": "S",
          "SSSS": "P",
          "SSRR": "R",  # New response for Kris's repetitive pattern
      }
      if last_four in pattern_responses_kris:
          return pattern_responses_kris[last_four]

  # If no clear patterns, respond adaptively
  last_play = opponent_history[-1] if opponent_history else ""
  if last_play:
      return ideal_response[last_play]

  # If no history, start with a default move
  return "R"
