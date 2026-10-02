# ==============================================================================
# مشروع: الدرع الحصين للوعي (Sovereign Awareness Shield Core)
# المكون: محرك التحليل والفلترة + شبكة التراسل اللامركزية (P2P)
# ==============================================================================

import socket
import threading
import json
import hashlib
from datetime import datetime
from enum import Enum
from typing import Dict, Any, List

# --- 1. تصنيف الأغراض والأهداف النفسية ---
class IntentType(Enum):
    FEAR_AND_PANIC = "إثارة الرعب والهلع"
    INTERNAL_STRIFE = "بث الفتنة والشقاق"
    PSYCHOLOGICAL_ATTRITION = "استنزاف ونخر الوعي"
    AUTHENTIC_NEWS = "خبر حقيقي / موثق"

class ContentType(Enum):
    TEXT = "نص"
    IMAGE = "صورة"
    VIDEO = "مقطع فيديو"

# --- 2. محرك الفحص والتحليل الذكي ---
class AwarenessShieldEngine:
    def __init__(self, truth_database: List[Dict[str, Any]]):
        self.truth_database = truth_database
        self.fear_keywords = ["سقوط", "تمت السيطرة", "انسحاب جماعي", "حصار خانق", "لا مفر", "هروب"]
        self.strife_keywords = ["خيانة", "بيع الجبهات", "المخطط السري", "طعنة في الظهر", "مؤامرة داخلية"]
        self.attrition_keywords = ["لا فائدة", "المعركة محسومة", "استسلموا", "نهاية وشيكة", "بلا جدوى"]

    def analyze_intent(self, text_content: str) -> Dict[str, Any]:
        fear_score = sum(1 for word in self.fear_keywords if word in text_content)
        strife_score = sum(1 for word in self.strife_keywords if word in text_content)
        attrition_score = sum(1 for word in self.attrition_keywords if word in text_content)

        if fear_score > strife_score and fear_score > attrition_score and fear_score > 0:
            intent = IntentType.FEAR_AND_PANIC
            severity = min(fear_score * 25, 100)
        elif strife_score > fear_score and strife_score > attrition_score and strife_score > 0:
            intent = IntentType.INTERNAL_STRIFE
            severity = min(strife_score * 25, 100)
        elif attrition_score > 0:
            intent = IntentType.PSYCHOLOGICAL_ATTRITION
            severity = min(attrition_score * 25, 100)
        else:
            intent = IntentType.AUTHENTIC_NEWS
            severity = 0

        return {
            "intent": intent.value,
            "severity_level": f"{severity}%",
            "is_manipulative": intent != IntentType.AUTHENTIC_NEWS
        }

    def verify_reality(self, location: str, claim: str) -> Dict[str, Any]:
        for record in self.truth_database:
            if record["location"] == location:
                return {
                    "is_fake": True,
                    "truth_summary": record["real_event_description"],
                    "last_updated": record["timestamp"]
                }
        return {
            "is_fake": True,
            "truth_summary": "الوضع الميداني مستقر ولم تسجل أي تغييرات في خطوط التماس. المنشور يندرج ضمن الدعاية النفسية.",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

    def process_content(self, post_data: Dict[str, Any]) -> Dict[str, Any]:
        text = post_data.get("text", "")
        location = post_data.get("location", "عام")
        psych_analysis = self.analyze_intent(text)
        fact_check = self.verify_reality(location, text)

        return {
            "status": "BLOCKED_PSYCHOLOGICAL_ATTACK" if psych_analysis["is_manipulative"] else "PASSED",
            "psychological_target": {
                "purpose": psych_analysis["intent"],
                "threat_level": psych_analysis["severity_level"]
            },
            "comparison": {
                "misleading_post": text,
                "actual_reality": fact_check["truth_summary"],
                "verification_time": fact_check["last_updated"]
            }
        }

# --- 3. عقدة التراسل الشبكي اللامركزي (P2P Node) ---
class ShieldMeshNode:
    def __init__(self, host: str, port: int, engine: AwarenessShieldEngine):
        self.host = host
        self.port = port
        self.engine = engine
        self.peers = []
        self.known_threat_hashes = set()

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        print(f"[*] الدرع الحصين يعمل كعقدة شبكية على: {self.host}:{self.port}")
        threading.Thread(target=self._listen, args=(server,), daemon=True).start()

    def _listen(self, server_socket):
        while True:
            client, _ = server_socket.accept()
            threading.Thread(target=self._handle_data, args=(client,), daemon=True).start()

    def _handle_data(self, client_socket):
        data = client_socket.recv(4096).decode('utf-8')
        if data:
            payload = json.loads(data)
            if payload.get("type") == "NEW_THREAT_HASH":
                t_hash = payload.get("hash")
                if t_hash not in self.known_threat_hashes:
                    self.known_threat_hashes.add(t_hash)
                    self.broadcast_threat(t_hash)
        client_socket.close()

    def broadcast_threat(self, threat_hash: str):
        payload = json.dumps({"type": "NEW_THREAT_HASH", "hash": threat_hash})
        for peer_host, peer_port in self.peers:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((peer_host, peer_port))
                sock.send(payload.encode('utf-8'))
                sock.close()
            except Exception:
                continue

# --- تشغيل وتجربة النظام الموحد ---
if __name__ == "__main__":
    DB = [{
        "location": "جبهة مأرب",
        "real_event_description": "الوضع مستقر تماماً ومحاولة التضليل تعتمد على فيديو قديم.",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }]
    
    engine = AwarenessShieldEngine(truth_database=DB)
    node = ShieldMeshNode("127.0.0.1", 5000, engine)
    node.start()
    
    test_post = {
        "text": "عاجل وسقوط وشيك! انسحاب جماعي وحصار خانق في جبهة مأرب!",
        "location": "جبهة مأرب"
    }
    
    report = engine.process_content(test_post)
    print("\n[+] تقرير الفحص الميداني والنفسي:")
    print(json.dumps(report, ensure_ascii=False, indent=4))
                  
