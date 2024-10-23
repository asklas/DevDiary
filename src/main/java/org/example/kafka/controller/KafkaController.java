package org.example.kafka.controller;

import org.example.kafka.model.UserMessage;
import org.example.kafka.producer.ProducerService;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class KafkaController {

    @Autowired
    private ProducerService producerService;

    @PostMapping("/send")
    public void sendMessage(@RequestBody UserMessage userMessage) {
        try {
            String jsonMessage = new ObjectMapper().writeValueAsString(userMessage);
            producerService.sendMessage("user-topic", jsonMessage);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }
}

