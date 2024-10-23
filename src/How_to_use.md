[원문 보기](https://devocean.sk.com/blog/techBoardDetail.do?ID=164016)

# docker-compose.yml 파일 세부 사항

---
version:
docker-compose 버젼을 지정한다. 여기서는 2 라고 기술했다.

services:
docker-compose의 경우 docker 컨테이너로 수행될 서비스들은 services 하위에 기술한다.

zookeeper:
서비스 이름을 zookeeper-1, 2, 3 로 작성했다.
service 하위에 작성하면 서비스 이름으로 동작한다.

image:
우리는 여기서 confluentinc/cp-zookeeper:latest 를 이용할 것이다.
참고로 실전에서 사용하려면 latest 라는 태그를 사용하지 말고, 정확히 원하는 버젼을 기술해서 사용하길 추천한다.
latest라고 태그를 지정하면, 매번 컨테이너를 실행할때마다 최신버젼을 다운받아 실행하므로 변경된 버젼으로 인해 원하지 않는 결과를 볼 수 있다. (주의 !!!)

environment:
confluentinc 는 몇가지 환경 변수를 설정할 수 있다.
environment 하위에 필요한 환경을 작성하자.

ZOOKEEPER_SERVER_ID:
zookeeper 클러스터에서 유일하게 주키퍼를 식별할 아이디이다.
동일 클러스터 내에서 이 값은 중복되면 안된다. 단일 브로커이기 때문에 이 값은 의미가 없다.

ZOOKEEPER_CLIENT_PORT:
zookeeper_client_port를 지정한다. 여기서는 기본 주키퍼의 포트인 2181로 지정한다.
즉 컨테이너 내부에서 주키퍼는 2181로 실행된다.

ZOOKEEPER_TICK_TIME:
zookeeper이 클러스터를 구성할때 동기화를 위한 기본 틱 타임을 지정한다.
millisecond로 지정할 수 있으며 여기서는 2000으로 설정했으니 2초가 된다.

ZOOKEEPER_INIT_LIMIT:
주키퍼 초기화를 위한 제한 시간을 설정한다.
주키퍼 클러스터는 쿼럼이라는 과정을 통해서 마스터를 선출하게 된다. 이때 주키퍼들이 리더에게 커넥션을 맺을때 지정할 초기 타임아웃 시간이다.
타임아웃 시간은 이전에 지정한 ZOOKEEPER_TICK_TIME 단위로 설정된다.
우리는 ZOOKEEPER_TICK_TIME을 2000으로 지정했고, ZOOKEEPER_INIT_LIMIT을 5로 잡았으므로 2000 * 5 = 10000 밀리세컨이 된다. 즉, 10초가 된다.
이 옵션은 멀티 브로커에서 유효한 속성이다.

ZOOKEEPER_SYNC_LIMIT:
이 시간은 주키퍼 리더와 나머지 서버들의 싱크 타임이다.
이 시간내 싱크응답이 들어오는 경우 클러스터가 정상으로 구성되어 있늠을 확인하는 시간이다.
여기서 2로 잡았으므로 2000 * 2 = 4000 으로 4초가 된다.
이 옵션은 멀티 브로커에서 유효한 속성이다.

kafka
kafka 브로커 이름을 지정한다.

image:
kafka 브로커는 confluentinc/cp-kafka:latest 를 이용하였다.
역시 태그는 latest보다는 지정된 버젼을 사용하는것을 추천한다.

depends_on:
docker-compose 에서는 서비스들의 우선순위를 지정해 주기 위해서 depends_on 을 이용한다.
zookeeper 라고 지정하였으므로, kafka는 zookeeper이 먼저 실행되어 있어야 컨테이너가 올라오게 된다.

ports:
kafka 브로커의 포트를 의미한다.
외부포트:컨테이너내부포트 형식으로 지정한다.

environment:
kafka 브로커를 위한 환경 변수를 지정한다.

KAFKA_BROKER_ID:
kafka 브로커 아이디를 지정한다. 유니크해야하며 지금 예제는 단일 브로커기 때문에 없어도 무방하다.

KAFKA_ZOOKEEPER_CONNECT:
kafka가 zookeeper에 커넥션하기 위한 대상을 지정한다.
여기서는 zookeeper(서비스이름):2181(컨테이너내부포트) 로 대상을 지정했다.

KAFKA_ADVERTISED_LISTENERS:
외부에서 접속하기 위한 리스너 설정을 한다.

KAFKA_LISTENER_SECURITY_PROTOCOL_MAP:
보안을 위한 프로토콜 매핑이디. 이 설정값은 KAFKA_ADVERTISED_LISTENERS 과 함께 key/value로 매핑된다.

KAFKA_INTER_BROKER_LISTENER_NAME:
도커 내부에서 사용할 리스너 이름을 지정한다.
이전에 매핑된 PLAINTEXT가 사용되었다.

KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR:
이 값은 트랜잭션 상태에서 복제 계수를 지정한다. 우리는 단순하게 작업하기 위해서 복제 계수를 1로 설정했다.

KAFKA_TRANSACTION_STATE_LOG_MIN_ISR:
트랜잭션 최소 ISR(InSyncReplicas 설정) 을 지정하는 것으로 우리는 단순하게 작업하기 위해서 복제 계수를 1로 설정했다

# docker 실행 명령어

---
`docker-compose -f docker-compose.yaml up -d `
> 1. -f <설정파일>을 통해서 우리가 작성한 설정으로 docker-compose를 실행한다.
>2. up 옵션을 통해 docker-compos 를 실행한다.
>3. -d 옵션은 detach 모드로 컨테이너를 백그라운드로 실행하게 해준다.

`docker ps `
>정상적으로 실행되었는지 확인하기 위해 로그를 출력한다.

```
docker-compose exec kafka-1 kafka-topics --create --topic my-topic --bootstrap-server kafka-1:9092 --replication-factor 3 --partitions 2
```
>docker-compose:
>명령어를 수행한다.
>
>exec:
>컨테이너 내에서 커맨드를 수행하도록 한다.
>
>kafka-1:
>우리가 설정으로 생성한 브로커(서비스) 이름이다.
>
>kafka-topics:
>카프카 토픽에 대한 명령을 실행한다.
>
>--create:
>토픽을 생성하겠다는 의미이다.
>
>--topic :
>생성할 토픽 이름을 지정한다.
>
>--bootstrap-server service:port
>bootstrap-server는 kafka-1 브로커 서비스를 나타낸다. 이때 서비스:포트 로 지정하여 접근할 수 있다.
>
>--replication-factor 1:
>복제 계수를 지정한다.
>여기서는 1로 지정했다.
>
>--partition:
>토픽내에 파티션 개수를 지정한다.

```
docker-compose exec kafka-1 kafka-topics --describe --topic my-topic --bootstrap-server kafka-1:9092 
```
>docker-compose:
명령어를 수행한다.
> 
>exec:
>컨테이너 내에서 커맨드를 수행하도록 한다.
>
>kafka-1:
>우리가 설정으로 생성한 브로커(서비스) 이름이다.
>
>kafka-topics:
>카프카 토픽에 대한 명령을 실행한다.
>
>--describe:
>생성된 토픽에 대한 상세 설명을 보여달라는 옵션이다.
>
>--topic :
>생성한 토픽 이름을 지정한다.
>
>--bootstrap-server service:port
>bootstrap-server는 kafak-1 브로커 서비스를 나타낸다. 이때 서비스:포트 로 지정하여 접근할 수 있다.
>결과로 kafka-1브로커의 토픽이름, 아이디, 복제계수, 파티션, 리더, 복제정보, isr 등을 확인할 수 있다.
>복제 계수는 3으로 지정되었다.
>그리고 파티션은 2개로 0, 1 이 있다.
>Leader의 결과를 통해서 해당 파티션의 리더가 어떤 브로커인지 알려준다.
>Replicas 는 데이터 복제에 대해서 알려준다.
>Isr: In sync replica 에 대해서 알려준다. (동기화된 복제본임을 알려준다.)

```
$ docker-compose exec kafka-1 bash
[appuser@571d813de396 ~]$ kafka-console-consumer --topic my-topic --bootstrap-server kafka-1:9092

$ docker-compose exec kafka-1 bash 
[appuser@571d813de396 ~]$ kafka-console-producer --topic my-topic --broker-list kafka-1:9092
>hello
>this is producer

hello
this is producer

$ docker-compose down
```
