package org.example.kafka.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.stereotype.Service;
import org.example.kafka.model.UserMessage;

@Service
public class MessageService {
    private final ObjectMapper objectMapper = new ObjectMapper();

    public String serialize(UserMessage userMessage) throws JsonProcessingException {
        return objectMapper.writeValueAsString(userMessage);
    }

    public UserMessage deserialize(String message) throws JsonProcessingException {
        return objectMapper.readValue(message, UserMessage.class);
    }
}
