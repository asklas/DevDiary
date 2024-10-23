package org.example.kafka.consumer;

import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
public class ConsumerService {

    @KafkaListener(topics = "user-topic", groupId = "your-group-id")
    public void listen(String message) {
        System.out.println("Received Message: " + message);
    }
}