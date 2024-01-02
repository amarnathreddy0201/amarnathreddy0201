#include <iostream>
// #################################### DIsk image transferring

#include <Poco/Net/HTTPClientSession.h>
#include <Poco/Net/HTTPRequest.h>
#include <Poco/Net/HTTPResponse.h>
#include <Poco/Path.h>
#include <Poco/URI.h>
#include <iostream>
#include <string>
#include <Poco/JSON/JSON.h>
#include <Poco/JSON/Parser.h>
#include <Poco/Net/HTMLForm.h>

#include <Poco/Base64Encoder.h>
#include <Poco/Net/HTMLForm.h>
#include <Poco/Net/StringPartSource.h>
#include <Poco/StreamCopier.h>
#include <Poco/Buffer.h>
#include <Poco/Net/FilePartSource.h>
#include <Poco/Net/PartSource.h>

#include <Windows.h>
#include <vector>

#include <opencv2/opencv.hpp>
#include <opencv2/calib3d/calib3d.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/core/core.hpp>


#define SPDLOG_ACTIVE_LEVEL SPDLOG_LEVEL_TRACE
#include <spdlog/spdlog.h>
#include <spdlog/sinks/stdout_sinks.h>
#include <chrono>
#include <typeinfo>
#include <string>


int main() {
    const char host[10] = "127.0.0.1";

    const int port = 4003;

    Poco::Net::HTTPResponse res;

    // prepare path
    std::string path;

    path = "/images/";

    Poco::Net::HTTPClientSession session(host, port);
    session.setKeepAlive(true);

    Poco::Net::HTTPRequest req(Poco::Net::HTTPRequest::HTTP_POST, path, Poco::Net::HTTPMessage::HTTP_1_1);

    

    req.setContentType("application/json");

    

    //HTTPRequest request(HTTPRequest::HTTP_POST, "/fileupload/upload_file.php", HTTPMessage::HTTP_1_1);
    Poco::Net::HTMLForm form;
    form.setEncoding(Poco::Net::HTMLForm::ENCODING_MULTIPART);
    form.addPart("photo1", new Poco::Net::FilePartSource("C:/Amar/2_plots_testing/all1.png"));
    form.prepareSubmit(req);

    
    form.write(session.sendRequest(req));

    //Poco::Net::HTTPResponse res;
    std::istream& is = session.receiveResponse(res);
    Poco::StreamCopier::copyStream(is, std::cout);
}
